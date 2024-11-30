<<<<<<< HEAD
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
=======
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
>>>>>>> 04cc55d8a888afae391c43df75b3ccf4ebf93344
