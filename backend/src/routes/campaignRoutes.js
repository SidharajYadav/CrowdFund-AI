import express from "express";
import {
  createCampaign,
  getCampaigns,
} from "../controllers/campaignController.js";
import { authenticate } from "../middleware/authMiddleware.js";

const router = express.Router();
router.post("/", authenticate, createCampaign);
router.get("/", getCampaigns);
 
export default router;
 
  
