import axios from "axios";

const ML_API_URL = process.env.ML_API_URL;

export const getMLPrediction = async (data) => {
  try {
    const response = await axios.post(`${ML_API_URL}/predict`, data);
    return response.data;
  } catch (err) {
    console.error("Error calling ML API:", err.message);
    throw new Error("Failed to fetch ML prediction");
  }
};  
 
   
 
