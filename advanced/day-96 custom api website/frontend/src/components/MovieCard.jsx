import React, { useState } from "react";
import api from "./api";

function MovieCard() {
  const [movies, setMovies] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchMovies = () => {
    setLoading(false);
    api
      .get("/movies")
      .then((resp) => {
        setMovies(resp.data.docs);
        setError(null);
      })
      .catch((err) => {
        console.error("Error: ", err);
        setError("Failed to fetch movies. Please try again later.");
      })
      .finally(() => {
        setLoading(true);
      });
  };

  return (
    <>
      <div className="text-center mb-6">
        <button
          onClick={fetchMovies}
          className="bg-yellow-400 cursor-pointer hover:bg-yellow-500 text-black font-bold py-2 px-4 rounded-lg transition"
        >
          {loading ? "Fetch Movies 🍿" : "Loading ..."}
        </button>
      </div>

      {error && (
        <div className="bg-red-500 text-white p-4 mb-4 rounded-md text-center">
          {error}
        </div>
      )}

      <div className="grid gap-4 md:grid-cols-2">
        {movies.map((movie) => (
          <div
            key={movie._id}
            className="bg-gray-800 rounded-xl p-4 shadow-md hover:shadow-lg transition"
          >
            <h2 className="text-xl font-semibold">{movie.name}</h2>
            <p className="text-sm text-gray-400">
              Runtime: {movie.runtimeInMinutes} mins | Budget: $
              {movie.budgetInMillions}M
            </p>
            <p className="text-sm text-gray-400">
              Revenue: ${movie.boxOfficeRevenueInMillions} Million | Score:
              {movie.rottenTomatoesScore} 🍅
            </p>
          </div>
        ))}
      </div>
    </>
  );
}

export default MovieCard;
