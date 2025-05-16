import React, { useState } from "react";
import api from "./api";
import BookChapter from "./BookChapter";

export default function BookCard() {
  const [books, setBooks]   = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError]     = useState(null);

  const fetchBooks = async () => {
    try {
      setLoading(true);
      const { data } = await api.get("/book");
      setBooks(data.docs);
      setError(null);
    } catch (err) {
      setError("Failed to fetch books.");
    } finally {
      setLoading(false);
    }
  };

  const clearBooks = () => {
    setBooks([]);
    setError(null);
  };

  return (
    <div className="max-w-4xl mx-auto p-6 bg-gray-900 min-h-screen text-white">
      <div className="flex justify-center items-center gap-4 mb-8">
        <button
          onClick={fetchBooks}
          disabled={loading}
          className={`py-2 px-4 rounded shadow font-bold transition
            ${loading 
              ? "bg-yellow-300 cursor-wait text-black" 
              : "bg-yellow-400 hover:bg-yellow-500 text-black"}
          `}
        >
          {loading ? "Fetching…" : "Fetch Books"}
        </button>

        {(books.length > 0 || error) && (
          <button
            onClick={clearBooks}
            className="py-2 px-4 rounded shadow bg-red-500 hover:bg-red-600 text-white font-bold transition"
          >
            Clear All
          </button>
        )}
      </div>

      {error && (
        <div className="bg-red-700 text-white p-3 mb-6 rounded text-center">
          {error}
        </div>
      )}

      <div className="grid gap-6 md:grid-cols-1">
        {books.map((book) => (
          <div
            key={book._id}
            className="bg-gray-800 rounded-xl p-6 shadow-lg hover:shadow-2xl transition"
          >
            <BookChapter
              bookID={book._id}
              bookName={book.name}
            />
          </div>
        ))}

        {(!loading && books.length === 0 && !error) && (
          <p className="text-center text-gray-500 italic col-span-full">
            No books loaded. Click “Fetch Books” to get started.
          </p>
        )}
      </div>
    </div>
  );
}
