let drink_ingredients = []
let answered = false;

function formatFeedback() {
    let feedback = '<p class="text-danger">Incorrect. The correct answer is: '
    question.correct_answer.forEach((ingredient, i) => {
        feedback += ingredient[1] + " " + ingredient[0] + ", ";
    })
    feedback = feedback.slice(0, -2);
    feedback += '</p>';
    return feedback;
}

function addContent() {
    event.preventDefault(); // Prevent default form submission

    // Disable the submit button
    $("#submit-button").prop("disabled", true);
    $("#submit").prop("disabled", true);

    // Clear previous feedback
    $("#feedback").empty();

    let correctAnswer = question.correct_answer;
    let questionId = question.id; // Access question ID directly from the question object

    // Log selected option
    console.log('Selected option:', drink_ingredients);

    // Compare selected option's ID with correct answer's ID
    let correct = true;
    if(drink_ingredients.length !== question.correct_answer.length) {
        $("#feedback").append(formatFeedback());
        correct = false;
    }
    else {
        drink_ingredients.forEach((ingredient, i) => {
            if (ingredient[0] !== question.correct_answer[i][0] || ingredient[1] !== question.correct_answer[i][1]) {
                correct = false;
            }
        })
        if (correct) {
            $("#feedback").append('<p class="text-success">Correct!</p>');
        }
        else {
            $("#feedback").append(formatFeedback());
        }
    }

    // Send data to the server using AJAX
    $.ajax({
        type: "POST",
        url: "/submit-answer/" + questionId,
        data: {
            questionId: questionId,
            selectedOption: JSON.stringify(drink_ingredients),
            correctAnswer: JSON.stringify(correctAnswer)
        },
        success: function(response) {
            console.log(response); // Log the response from the server
        },
        error: function(xhr, status, error) {
            console.error(error); // Log any errors
        }
    });
    answered = true;
    enableNavigationButton();
}

// Function to enable navigation button if the question is answered
function enableNavigationButton() {
    console.log('Enabling navigation button'); // Log to verify function call

    // Check if the question is answered
    if (answered) {
        $(".next-button-link").removeClass("disabled");
    }
}


// Function to disable navigation button
function disableNavigationButton() {
    $(".next-button-link").addClass("disabled");
}

$( document ).ready(function() {
    $("#drink").append(renderDrink(drink_ingredients));

    disableNavigationButton();

    legend.forEach(ingredient => {
        const imageName = ingredient.image.split("/").pop();
        ingredient.image = `/static/media/legend/${imageName}`;
		$(".ingredients-legend").append(`<li>
			<div class="legend-ingredient" ondragover="allowDrop(event)">
                <img
                    src="${ingredient.image}"
                    class="legend-image"
                    alt="${ingredient.name}" 
                    draggable="true" ondragstart="drag(event)"/>
                </div>
                ${ingredient.name}
		</li>`)
    });

    $("#reset").click(function() {
        if(answered) {
            return;
        }
        drink_ingredients = [];
        $("#drink").empty();
        $("#drink").append(renderDrink(drink_ingredients));
        $( ".legend-ingredient" ).draggable({ revert: "invalid", helper: "clone" });
        $( ".ingredients-list" ).droppable({
            accept: ".legend-ingredient",
            drop: drop_function
        });
    });

    $("#submit").click(function() {
        addContent();
    });

    $( ".legend-ingredient" ).draggable({ revert: "invalid", helper: "clone" });
    $( ".ingredients-list" ).droppable({
        accept: ".legend-ingredient",
        drop: drop_function
    });
});

function drop_function(event, ui) {
    let ingredientName = ui.draggable.find("img").attr("alt");
            if(ingredientName === "Steamed Milk") {
                ingredientName = "milk"
            }
            ingredientName = ingredientName.toLowerCase();
            if (drink_ingredients.length == 0) {
                drink_ingredients.push([ingredientName, 1]);
            }
            else if (drink_ingredients[drink_ingredients.length - 1][0] === ingredientName) {
                drink_ingredients[drink_ingredients.length - 1][1] += 1;
            } else {
                drink_ingredients.push([ingredientName, 1]);
            }
            $(this).empty();
            $(this).replaceWith(renderDrink(drink_ingredients));
            $( ".ingredients-list" ).droppable({
                accept: ".legend-ingredient",
                drop: drop_function
            });
}

function allowDrop(ev){ev.preventDefault();}
function drag(ev){ev.dataTransfer.setData("text", ev.target.id)}

function renderDrink(drink_ingredients) {
    let count = 9;
    const ingredientsList = document.createElement('div');
    ingredientsList.classList.add('ingredients-list');
    drink_ingredients.forEach((ingredientArray, index) => {
        const ingredientName = ingredientArray[0];
        const ingredientQuantity = ingredientArray[1];
        for (let i = 0; i < ingredientQuantity; i+= 1) {
            const ingredient = document.createElement('img');
            ingredient.src = `/static/media/legend/${ingredientName}.png`;
            if(ingredientName === "foam" && i === ingredientQuantity - 1 && index === drink_ingredients.length - 1) {
                ingredient.src = `/static/media/legend/foam-top.png`;
            }
            ingredient.alt = ingredientName;
            ingredient.classList.add('ingredient-image');
            ingredientsList.prepend(ingredient);
            count -=1;
        }
    });
    while (count > 0) {
        const ingredient = document.createElement('img');
        ingredient.src = `/static/media/legend/empty.png`;
        ingredient.alt = "empty";
        ingredient.classList.add('ingredient-image');
        ingredientsList.prepend(ingredient);
        count -= 1;
    }
    return ingredientsList;
}