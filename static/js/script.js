$(document).ready(function() {
    $('.accordion').click(function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
});

function resetDrink(url, ingredients) {
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(ingredients)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Drink reset successfully!');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Failed to reset drink');
    });
}

function changeSlide(drinkId, direction) {
    var slides = document.querySelectorAll('[id^="slide-' + drinkId + '-"]');
    var currentSlideIndex = Array.from(slides).findIndex(slide => slide.style.display !== 'none');
    var newSlideIndex = direction === 'next' ? currentSlideIndex + 1 : currentSlideIndex - 1;

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
            displayIngredients(element);
        })
        .catch(error => {
            console.error('Error fetching drinks:', error);
        });
    } else {
        if (element.isShowingIngredients) {
            displayDrinkName(element, title);
        } else {
            displayIngredients(element);
        }
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

        const ingredientsList = document.createElement('ul');
        ingredientsList.classList.add('ingredients-list');
        
        drink.ingredients.forEach(ingredientArray => {
            const ingredientItem = document.createElement('li');
            ingredientItem.classList.add('ingredient');
            const ingredientName = ingredientArray[0];
            const ingredientQuantity = ingredientArray[1];
            ingredientItem.textContent = `${ingredientName} x${ingredientQuantity}`;
            ingredientsList.appendChild(ingredientItem);
        });

        drinkDiv.appendChild(ingredientsList);
        element.appendChild(drinkDiv);
    });
}
