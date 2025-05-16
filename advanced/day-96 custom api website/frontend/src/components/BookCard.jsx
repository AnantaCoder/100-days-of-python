import React, { useState } from "react";
import api from "./api";

function BookCard() {
  const [books, setBooks] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchBooks = () => {
    setLoading(false);
    api
      .get("/book")
      .then((resp) => {
        setBooks(resp.data.docs);
        setError(null);
      })
      .catch((err) => {
        console.error("Error: ", err);
        setError("Failed to fetch books. Please try again later.");
      })
      .finally(() => {
        setLoading(true);
      });
  };

  return (
    <>
      <div className="text-center mb-6">
        <button
          onClick={fetchBooks}
          className="bg-yellow-400 cursor-pointer hover:bg-yellow-500 text-black font-bold py-2 px-4 rounded-lg transition"
        >
          {loading ? "Fetch Books 📘" : "Loading..."}
        </button>
      </div>

      {error && (
        <div className="bg-red-500 text-white p-4 mb-4 rounded-md text-center">
          {error}
        </div>
      )}

      <div className="grid gap-4 md:grid-cols-2">
        {books.map((book) => (
          <div
            key={book._id}
            className="bg-gray-800 rounded-xl p-4 shadow-md hover:shadow-lg transition"
          >
            <h2 className="text-xl font-semibold">{book.name}</h2>
          </div>
        ))}
      </div>
    </>
  );
}

export default BookCard;
