import Campaign from "../models/Campaign.js";

export const createCampaign = async (req, res) => {
  try {
    const campaign = new Campaign(req.body); 
    await campaign.save();
    res.status(201).json(campaign);
  } catch (err) {
    res.status(500).json({ error: "Failed to create campaign" });
  }
};

export const getCampaigns = async (req, res) => {
  try {
    const campaigns = await Campaign.find();
    res.status(200).json(campaigns);
  } catch (err) {
    res.status(500).json({ error: "Failed to fetch campaigns" });
  }
};
 
