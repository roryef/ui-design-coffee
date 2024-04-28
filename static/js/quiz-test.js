let drink_ingredients = []

$( document ).ready(function() {
    $("#drink").append(renderDrink(drink_ingredients));

    legend.forEach(ingredient => {
        const imageName = ingredient.image.split("/").pop();
        ingredient.image = `/static/media/legend/${imageName}`;
		$(".legend").append(`<li>
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

    $("#submit").click(function() {
        let correct = true;
        if(drink_ingredients.length !== data.ingredients.length) {
            alert("Incorrect! Try again.");
            drink_ingredients = [];
            $("#drink").empty();
            $("#drink").append(renderDrink(drink_ingredients));
            correct = false;
            $( ".legend-ingredient" ).draggable({ revert: "invalid", helper: "clone" });
            $( ".ingredients-list" ).droppable({
                accept: ".legend-ingredient",
                drop: drop_function
            });
            return;
        }
        drink_ingredients.forEach((ingredient, i) => {
            if (ingredient[0] !== data.ingredients[i][0] || ingredient[1] !== data.ingredients[i][1]) {
                correct = false;
            }
        })
        if (correct) {
            alert("Correct!");
        }
        else {
            alert("Incorrect! Try again.");
            drink_ingredients = [];
            $("#drink").empty();
            $("#drink").append(renderDrink(drink_ingredients));
            $( ".legend-ingredient" ).draggable({ revert: "invalid", helper: "clone" });
                $( ".ingredients-list" ).droppable({
                    accept: ".legend-ingredient",
                    drop: drop_function
                });
        }
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