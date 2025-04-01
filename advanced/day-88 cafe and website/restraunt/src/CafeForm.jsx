import React from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';

function CafeForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    try {
      const response = await axios.post('http://localhost:8000/add', data);
      console.log('Success:', response.data);
    } catch (error) {
      console.error('Error adding cafe:', error);
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow-lg">
      <h2 className="text-2xl font-bold mb-6 text-center">Add a Cafe</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="mb-4">
          <label htmlFor="name" className="block text-gray-700 font-medium mb-2">
            Name
          </label>
          <input
            id="name"
            type="text"
            {...register('name', { required: 'Name is required' })}
            className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
          />
          {errors.name && <p className="text-red-500 text-sm mt-1">{errors.name.message}</p>}
        </div>

        <div className="mb-4">
          <label htmlFor="map_url" className="block text-gray-700 font-medium mb-2">
            Map URL
          </label>
          <input
            id="map_url"
            type="text"
            {...register('map_url', { required: 'Map URL is required' })}
            className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
          />
          {errors.map_url && <p className="text-red-500 text-sm mt-1">{errors.map_url.message}</p>}
        </div>

        <div className="mb-4">
          <label htmlFor="img_url" className="block text-gray-700 font-medium mb-2">
            Image URL
          </label>
          <input
            id="img_url"
            type="text"
            {...register('img_url', { required: 'Image URL is required' })}
            className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
          />
          {errors.img_url && <p className="text-red-500 text-sm mt-1">{errors.img_url.message}</p>}
        </div>

        <div className="mb-4">
          <label htmlFor="location" className="block text-gray-700 font-medium mb-2">
            Location
          </label>
          <input
            id="location"
            type="text"
            {...register('location', { required: 'Location is required' })}
            className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
          />
          {errors.location && <p className="text-red-500 text-sm mt-1">{errors.location.message}</p>}
        </div>

       
        <div className="mb-4">
          <label className="block text-gray-700 font-medium mb-2">Has Sockets?</label>
          <select
            {...register('has_sockets', { required: 'This field is required' })}
            className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
          >
            <option value="">Select an option</option>
            <option value="True">True</option>
            <option value="False">False</option>
          </select>
          {errors.has_sockets && <p className="text-red-500 text-sm mt-1">{errors.has_sockets.message}</p>}
        </div>

        <button
          type="submit"
          className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Add Cafe
        </button>
      </form>
    </div>
  );
}

export default CafeForm;
