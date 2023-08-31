const movies_api = "http://127.0.0.1:8000/";
const getMovies = async () => {
try {
  response = await fetch(movies_api);
  movies = await response.json();
}catch(error){
    console.log(error);
  return;
}

  movies.forEach((movie) => {
    document.querySelector(".movies-list").innerHTML += `
    <li>
    <a href="characters.html?id=${movie.id}">${movie.title}</a>
    </li>
    `;
  });
};

document.addEventListener("DOMContentLoaded", () => getMovies());
