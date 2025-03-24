# AuthenTick - Fact Checking Browser Extension

AuthenTick is a browser extension that helps users verify the credibility of news articles and claims found online. It integrates multiple fact-checking sources to provide real-time verification.

## Features
- **Fact Verification**: Uses Google Fact Check API, Snopes scraping, and News API to validate claims.
- **Browser Integration**: Works as an extension to analyze selected text or articles.
- **Multi-Source Comparison**: Aggregates results from different sources to provide a comprehensive analysis.
- **User-Friendly UI**: Simple and interactive design for seamless user experience.

## Technologies Used
- **Backend**: Flask
- **Frontend**: JavaScript (for browser extension integration)
- **APIs Used**:
  - Google Fact Check API
  - Snopes (scraped data)
  - News API

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Indhumathi-SivaShanmugam/AuthenTICK.git
   cd AuthenTick
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```
5. Load the extension in your browser:
   - Open Chrome and navigate to `chrome://extensions/`
   - Enable Developer Mode
   - Click on "Load unpacked" and select the `extension` folder

## Future Scope
- **Credibility Score**: Implement a scoring system for evaluating article reliability.
- **AI-Based Detection**: Use machine learning models for enhanced fake news detection.
- **More Fact-Checking Sources**: Integrate additional fact-checking platforms.
- **User Feedback Mechanism**: Allow users to contribute to credibility ratings.
