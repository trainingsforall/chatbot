const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// 👇 Mocked /chat route — doesn't use OpenAI
app.post("/chat", async (req, res) => {
  const { message } = req.body;
  res.json({ reply: `Pretend reply: You said "${message}"` });
});

// Optional: A root route to show the service is running
app.get("/", (req, res) => {
  res.send("✅ Chatbot mock server is running!");
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`✅ Server running on port ${PORT}`));
