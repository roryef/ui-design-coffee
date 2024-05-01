function addContent() {
    event.preventDefault(); // Prevent default form submission

    // Disable the submit button
    $("#submit-button").prop("disabled", true);
    // Disable all radio buttons
    $('input[name="answer"]').prop("disabled", true);

    // Clear previous feedback
    $("#feedback").empty();

    let selectedOption = $('input[name="answer"]:checked').val(); // Get selected option

    let correctAnswer = $('#correct-answer').val();
    let questionId = question.id; // Access question ID directly from the question object


    // Compare selected option's ID with correct answer's ID
    if (selectedOption === correctAnswer) {
        $("#feedback").append('<p class="text-success">Correct!</p>');
    } else {
        // Display the correct image URL if the answer is incorrect
        $("#feedback").append('<p class="text-danger">Incorrect. The correct answer is: ' + correctAnswer + ')</p>');
    }

    // Log selected option
    console.log('Selected option:', selectedOption);

    // Send data to the server using AJAX
    $.ajax({
        type: "POST",
        url: "/submit-answer/" + questionId,
        data: {
            questionId: questionId,
            selectedOption: selectedOption,
            correctAnswer: correctAnswer
        },
        success: function(response) {
            console.log(response); // Log the response from the server
        },
        error: function(xhr, status, error) {
            console.error(error); // Log any errors
        }
    });
}

function createDrink(drink_ingredients) {
    let count = 9;
    const ingredientsList = document.createElement('div');
    ingredientsList.classList.add('ingredients-list');
    drink_ingredients.forEach(ingredientArray => {
        const ingredientName = ingredientArray[0];
        const ingredientQuantity = ingredientArray[1];
        for (let i = 0; i < ingredientQuantity; i+= 1) {
            const ingredient = document.createElement('img');
            ingredient.src = `/static/media/legend/${ingredientName}.png`;
            if(ingredientName === "foam" && i === ingredientQuantity - 1) {
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

// Execute when the document is ready
drinks = [];
$(document).ready(function () {
    $("#submit-button").click(addContent);
    question.options.forEach(option => {
        drinks.push(createDrink(option.ingredients));
    });
    console.log(drinks)
    $(".img-label").each(function(i, obj) {
        obj.append(drinks[i]);
    });
});
