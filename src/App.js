import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

const App = () => {
  const [claim, setClaim] = useState('');
  const [result, setResult] = useState('');
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleClaimChange = (e) => {
    setClaim(e.target.value);
  };

  const handleCheckClaim = async () => {
    if (!claim.trim()) {
      setError('Please enter a claim to check.');
      return;
    }

    setLoading(true);
    setError('');
    setResult('');
    setArticles([]);

    try {
      // Request articles related to the claim using NewsAPI
      const response = await axios.get('https://newsapi.org/v2/everything', {
        params: {
          q: claim,
          apiKey: '1e9bbbc383874b31b5a070857dd05b3d', // Your API key
          sortBy: 'relevance',
          pageSize: 5,
        },
      });

      const data = response.data.articles;

      if (data.length === 0) {
        setResult('No relevant articles found.');
      } else {
        // Analyze the claim based on the fetched articles
        const fakeKeywords = ['debunk', 'false', 'misleading', 'hoax', 'not true'];
        const trueKeywords = ['true', 'fact', 'verified', 'correct', 'accurate'];

        let isFake = false;
        let isTrue = false;

        data.forEach((article) => {
          const title = article.title.toLowerCase();
          const description = article.description.toLowerCase();

          if (fakeKeywords.some((word) => title.includes(word) || description.includes(word))) {
            isFake = true;
          }

          if (trueKeywords.some((word) => title.includes(word) || description.includes(word))) {
            isTrue = true;
          }
        });

        if (isFake) {
          setResult('This claim is likely fake based on the articles.');
        } else if (isTrue) {
          setResult('This claim is likely true based on the articles.');
        } else {
          setResult('Unable to determine the authenticity of this claim from the articles.');
        }

        setArticles(data);
      }
    } catch (err) {
      setError('An error occurred while fetching data.');
    }

    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Fake News Detection</h1>
      <input
        type="text"
        value={claim}
        onChange={handleClaimChange}
        placeholder="Enter a claim to check..."
      />
      <button onClick={handleCheckClaim} disabled={loading}>
        {loading ? 'Checking...' : 'Check Claim'}
      </button>
      {error && <p className="error">{error}</p>}
      {result && <h2>{result}</h2>}

      {articles.length > 0 && (
        <div className="results">
          <h3>Related Articles:</h3>
          {articles.map((article, index) => (
            <div key={index} className="article">
              <h3>{article.title}</h3>
              <p>{article.description}</p>
              <a href={article.url} target="_blank" rel="noopener noreferrer">Read More</a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default App;
