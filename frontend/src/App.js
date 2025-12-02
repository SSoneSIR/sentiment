import { useState } from "react";
import axios from "axios";

function App() {
  const [review, setReview] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const res = await axios.post("http://127.0.0.1:8000/api/predict/", { review });
    setResult(res.data);
  };

  return (
    <div style={{ padding: 40 }}>
      <h2>Movie Review Sentiment</h2>
      <textarea
        value={review}
        onChange={(e) => setReview(e.target.value)}
        placeholder="Enter review..."
        rows={4}
        cols={50}
      />

      <br /><br />
      <button onClick={handleSubmit}>Predict</button>

      {result && (
        <div style={{ marginTop: 20 }}>
          <h3>Sentiment: {result.sentiment}</h3>
          <p>Confidence: {result.confidence}</p>
        </div>
      )}
    </div>
  );
}

export default App;
