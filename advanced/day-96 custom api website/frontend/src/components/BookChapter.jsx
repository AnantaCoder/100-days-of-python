import React, { useState } from "react";
import api from "./api";

export default function BookChapter({ bookID, bookName }) {
  const [chapters, setChapters] = useState([]);
  const [loading, setLoading]   = useState(false);
  const [error, setError]       = useState(null);

  const fetchChapters = async () => {
    try {
      setLoading(true);
      const { data } = await api.get(`/book/${bookID}/chapter`);
      setChapters(data.docs);
      setError(null);
    } catch (err) {
      setError("Failed to load chapters.");
    } finally {
      setLoading(false);
    }
  };

  const clearChapters = () => {
    setChapters([]);
    setError(null);
  };

  return (
    <div className="space-y-4">
      <h3 className="text-2xl font-bold text-emerald-300">{bookName}</h3>

      <div className="flex gap-2">
        <button
          onClick={fetchChapters}
          disabled={loading}
          className={`flex-1 py-2 rounded shadow text-white font-medium transition 
            ${loading 
              ? "bg-blue-400 cursor-wait" 
              : "bg-blue-600 hover:bg-blue-700"}
          `}
        >
          {loading ? "Loading…" : "Load Chapters"}
        </button>
        {(chapters.length > 0 || error) && (
          <button
            onClick={clearChapters}
            className="flex-1 py-2 rounded shadow bg-red-600 hover:bg-red-700 text-white font-medium transition"
          >
            Clear
          </button>
        )}
      </div>

      {/* Error */}
      {error && (
        <p className="text-red-400">{error}</p>
      )}

      {/* Chapter List */}
      {chapters.length > 0 ? (
        <ul className="grid gap-3 md:grid-cols-2">
          {chapters.map((ch, i) => (
            <li
              key={ch._id}
              className="bg-gray-800 p-3 rounded border border-gray-700 hover:border-blue-400 transition"
            >
              <span className="font-semibold">{i + 1}.</span> {ch.chapterName}
            </li>
          ))}
        </ul>
      ) : (
        !loading && !error && (
          <p className="text-gray-500 italic">No chapters loaded yet.</p>
        )
      )}
    </div>
  );
}
