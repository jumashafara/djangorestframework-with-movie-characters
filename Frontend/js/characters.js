const characters_api = "http://127.0.0.1:8000/characters";
const query_string = window.location.search;
const query_params = new URLSearchParams(query_string);

const getCharacters = async () => {
  try {
    response = await fetch(`${characters_api}/${query_params.get("id")}`);
    characters = await response.json();
  } catch (error) {
    document.querySelector(".error").innerHTML =
      "Could not fetch the characters";
      return
  }

  if (characters.length === 0) {
    document.querySelector(".error").innerHTML = "No characters found";
    return;
  }
  
  characters.forEach((character) => {
    document.querySelector(".characters-tbody").innerHTML += `
    <td>${character.name}</td>
    <td>${character.age}</td>
    <td>${character.first_appearance}</td>
    `;
  });
};

document.addEventListener("DOMContentLoaded", () => getCharacters());
