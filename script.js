// script.js
const cocktailButtonsContainer = document.getElementById('cocktailButtons');

// Fetch cocktail data from your local JSON file
fetch('cocktail-recipes.json')
    .then((response) => response.json())
    .then((data) => {
        data.forEach((cocktail) => {
            const button = document.createElement('button');
            button.textContent = cocktail.name;
            button.addEventListener('click', () => displayRecipe(cocktail));
            cocktailButtonsContainer.appendChild(button);
        });
    })
    .catch((error) => console.error('Error fetching data:', error));

function displayRecipe(cocktail) {
    // Display recipe details (ingredients, instructions) in recipeContainer
    recipeContainer.innerHTML = `
        <h2>${cocktail.name}</h2>
        <h3>${cocktail.summary}</h3>
        <h3>Ingredients:</h3>
        <ul>
            ${cocktail.ingredients.map((ingredient) => `<li>${ingredient}</li>`).join('')}
        </ul>
        <h3>Instructions:</h3>
        <p>${cocktail.instructions}</p>
        <img src='./${cocktail.image}'></>
    `;
}
















