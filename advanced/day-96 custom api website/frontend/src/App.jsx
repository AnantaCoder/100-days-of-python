import MovieCard from "./components/MovieCard";
import BookCard from "./components/BookCard";



const App = () => {
  

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <div className="min-h-screen bg-gray-900 text-white p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-6 text-center text-yellow-400">
          📚 Lord of the Rings Books
        </h1>
      <MovieCard/>
      <br />
      <BookCard/>
        </div>
    </div>
    </div>
  );
};

export default App;
