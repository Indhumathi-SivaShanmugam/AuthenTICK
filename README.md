# AuthenTICK-Fake News Detection and Credibility Checker

## Problem Statement
In today's digital age, misinformation spreads rapidly, leading to confusion and distrust. With the rise of fake news, there is an increasing need for tools that can assist users in discerning credible information from false claims. This project aims to address this issue by providing a tool that verifies claims and guides users toward reliable sources.

---

## Project Idea
The idea is to create a **browser extension** that:
- Reads out and highlights false claims detected in online articles.
- Provides a **credibility score** to help users assess the trustworthiness of a claim.
- Suggests **authenticated articles** or sources for further reference and clarification.

This extension will assist users in navigating the vast pool of online content while ensuring they consume verified and accurate information.

---

## Approach
1. **Claim Verification**: 
   - Use APIs to fetch related articles and determine whether a claim is credible or false based on specific keywords and context.
   - Assign a credibility score based on the consistency of the articles retrieved.

2. **Extension Functionality**:
   - Highlight detected false claims on web pages in real-time.
   - Provide a pop-up or sidebar displaying the credibility score and alternative, authentic articles.

3. **User Experience**:
   - A seamless and intuitive UI for users to verify claims without leaving the web page they are on.

4. **Future Enhancements**:
   - Incorporate NLP models for more accurate detection.
   - Add voice reading features for accessibility.

---

## Tech Stack
- **Frontend**: React.js (for the extension interface)
- **Backend**: Node.js and Express.js
- **API**: NewsAPI (for fetching relevant articles)
- **Styling**: Tailwind CSS
- **Additional Tools**:
  - Axios (for API calls)
  - NLP libraries (planned for future updates)

---

## Progress / Current Status
- The project is in its **initial stages**.
- Currently working on verifying headline claims using the **NewsAPI**.
- Articles related to claims are fetched and analyzed based on keywords for false or true claims.
- The next step is to build the browser extension interface and integrate real-time claim detection.

  ---
  ![image](https://github.com/user-attachments/assets/0eee25c4-2cec-4a8d-a60c-3cbc1e683b5c)


---

## Challenges Faced
1. **Relevance of Articles**: 
   - Not all fetched articles are directly relevant to the claims, leading to ambiguous results.

2. **Keyword Matching**:
   - The current logic relies heavily on keywords, which can result in false positives or negatives.

3. **API Limitations**:
   - Limited API request quotas can hinder testing and development progress.

4. **Integration with Browser Extension**:
   - Adapting the project to work seamlessly as an extension while maintaining real-time performance.

---

## Future Goals
- Refine the claim verification process using advanced machine learning models.
- Introduce a user-friendly interface for highlighting and presenting the credibility score.
- Build accessibility features like voice-based claim reading.
- Expand the database of authentic sources for better recommendations.

---
