import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import authRoutes from "./routes/authRoutes.js";
import campaignRoutes from "./routes/campaignRoutes.js"; 
import { errorHandler } from "./middleware/errorHandler.js"; 
import dotenv from "dotenv";
dotenv.config(); 
 
const app = express();
 
// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
 
// Routes
app.use("/api/auth", authRoutes);
app.use("/api/campaigns", campaignRoutes);

// Error Handling Middleware
app.use(errorHandler);

export default app;
