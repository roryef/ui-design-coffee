$(document).ready(function() {
    const answer_drinks = []
    const user_drinks = {}
    quiz.questions.forEach((question, index) => {
        answer_drinks.push(createDrink(question.correct_answer));
    });
    $(".answer-drink").each(function(i, obj) {
        obj.append(answer_drinks[i]);
    });
    console.log(user_data.quiz.answers);
    for (const [key, data] of Object.entries(user_data.quiz.answers)) {
        data.selected_option = JSON.parse(data.selected_option)
        user_drinks[key] = createDrink(data.selected_option)
    };
    $(".user-answer-drink").each(function(i, obj) {
        if (user_drinks[i+3] !== undefined) {
            obj.append(user_drinks[i+3]);
        }
    })
});

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
