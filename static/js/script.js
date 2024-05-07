let start_time = 0;
let hovered_1 = false;
let hovered_2 = false;
let hovered_3 = false;
let hovered_4 = false;

finished_1 = false;
finished_2 = false;


$(document).ready(function() {
    $('.accordion').click(function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
        start_time = new Date().getTime();
    });
});

function sendUserData(direction) {
    if(lesson.id == "intro") {
        let end_time = new Date().getTime();
        let time_spent = end_time - start_time;
        $.ajax({
            type: "POST",
            url: `/learn/update/${lesson.id}/`,
            data: JSON.stringify({
                completed: true,
                time_spent: time_spent,
                hovered_1: hovered_1,
                hovered_2: hovered_2,
                hovered_3: hovered_3,
                hovered_4: hovered_4,
            }),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response) {
                console.log(response); // Log the response from the server
                if(direction == "next")
                    window.location.href = "/learn/" + lesson.next + "/";
                else
                    window.location.href = "/";
            },
            error: function(xhr, status, error) {
                console.error(error); // Log any errors
            }
        });
    }
    else if (lesson.id == "review") {
        end_time = new Date().getTime();
        time_spent = end_time - start_time;
        $.ajax({
            type: "POST",
            url: `/learn/update/${lesson.id}/`,
            data: JSON.stringify({
                completed: true,
                time_spent: time_spent,
            }),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response) {
                console.log(response); // Log the response from the server
                if(direction == "next")
                    window.location.href = "/quiz/" + 1;
                else
                    window.location.href = "/learn/" + lesson.previous + "/";
            },
            error: function(xhr, status, error) {
                console.error(error); // Log any errors
            }
        });
    }
    else {
        if((!finished_1 || !finished_2) && direction == "next" && !completed) {
            alert("Please finish the drinks before moving on to the next lesson");
            return;
        }
        end_time = new Date().getTime();
        time_spent = end_time - start_time;
        $.ajax({
            type: "POST",
            url: `/learn/update/${lesson.id}/`,
            data: JSON.stringify({
                completed: true,
                time_spent: time_spent,
            }),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response) {
                console.log(response); // Log the response from the server
                if(direction == "next")
                    window.location.href = "/learn/" + lesson.next + "/";
                else
                    window.location.href = "/learn/" + lesson.previous + "/";
            },
            error: function(xhr, status, error) {
                console.error(error); // Log any errors
            }
        });
    }
}

function resetDrink(drinkId) {
    changeSlide(drinkId, 'next');
}


function changeSlide(drinkId, direction) {
    var slides = document.querySelectorAll('[id^="slide-' + drinkId + '-"]');
    var currentSlideIndex = Array.from(slides).findIndex(slide => slide.style.display !== 'none');
    var newSlideIndex = direction === 'next' ? currentSlideIndex + 1 : currentSlideIndex - 1;
    if (newSlideIndex == slides.length-1) {
        if(drinkId == 1) {
            finished_1 = true;
        }
        if(drinkId == 2) {
            finished_2 = true;
        }
    }
    if (newSlideIndex >= slides.length) newSlideIndex = 0;
    if (newSlideIndex < 0) newSlideIndex = slides.length - 1;

    showSlide(slides, newSlideIndex);
}

function goToSlide(drinkId, slideId) {
    var slides = document.querySelectorAll('[id^="slide-' + drinkId + '-"]');
    var newSlideIndex = Array.from(slides).findIndex(slide => slide.id === 'slide-' + drinkId + '-' + slideId);

    showSlide(slides, newSlideIndex);
}

function showSlide(slides, index) {
    slides.forEach(slide => slide.style.display = 'none');
    slides[index].style.display = 'block';

    var dots = slides[index].parentNode.parentNode.querySelector('.dots').children;
    Array.from(dots).forEach(dot => dot.classList.remove('active'));
    dots[index].classList.add('active');
}

document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.card').forEach(card => {
        var slides = card.querySelectorAll('.slide');
        var dots = card.querySelectorAll('.dot');

        if (slides.length && dots.length) {
            slides[0].style.display = 'block';
            dots[0].classList.add('active');
        }
    });
});

function toggleDrinks(element, title) {
    if (!element.drinksData) {
        fetch('/get-category-drinks?title=' + encodeURIComponent(title))
        .then(response => response.json())
        .then(data => {
            element.drinksData = data.drinks; 
            if(element.drinksData[0].name == "Espresso") {
                hovered_1 = true;
            }
            if(element.drinksData[0].name == "Macchiato") {
                hovered_2 = true;
            }
            if(element.drinksData[0].name == "Cappuccino") {
                hovered_3 = true;
            }
            if(element.drinksData[0].name == "Mocha") {
                hovered_4 = true;
            }
            displayIngredients(element);
            checkAllCategoriesClicked();
        })
        .catch(error => {
            console.error('Error fetching drinks:', error);
        });
    } else {
        if (!element.isShowingIngredients) {
            if(element.drinksData[0].name == "Espresso") {
                hovered_1 = true;
            }
            if(element.drinksData[0].name == "Macchiato") {
                hovered_2 = true;
            }
            if(element.drinksData[0].name == "Cappuccino") {
                hovered_3 = true;
            }
            if(element.drinksData[0].name == "Mocha") {
                hovered_4 = true;
            }
            displayIngredients(element);
            checkAllCategoriesClicked();
        }
    }
}

function checkAllCategoriesClicked() {
    // Check if all categories are clicked
    const allClicked = hovered_1 && hovered_2 && hovered_3 && hovered_4;
    const learnButton = document.querySelector('.quiz');
    if (allClicked) {
        // Enable the Learn button
        learnButton.classList.remove('disabled');
    } else {
        // Disable the Learn button
        learnButton.classList.add('disabled');
    }
}

function displayDrinkName(element, title) {

    element.innerHTML = '';
    element.isShowingIngredients = false;

    element.textContent = title;
    element.classList.add('category-card');
    element.classList.remove('drink-container');
}

function displayIngredients(element) {
    element.innerHTML = '';
    element.isShowingIngredients = true;

    element.classList.remove('category-card');
    element.classList.add('drink-container');

    // Display the ingredients
    element.drinksData.forEach(drink => {
        const drinkDiv = document.createElement('div');
        drinkDiv.classList.add('drink-name');

        const drinkName = document.createElement('p');
        drinkName.textContent = drink.name;
        drinkDiv.appendChild(drinkName);

        const ingredientsList = createDrink(drink.ingredients)

        drinkDiv.appendChild(ingredientsList);
        element.appendChild(drinkDiv);
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
