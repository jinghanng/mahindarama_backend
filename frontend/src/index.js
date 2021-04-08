// import "react-hot-loader";
import React from "react";
import ReactDOM from "react-dom";
import { CookiesProvider } from "react-cookie";

import App from "./components/App/App.jsx";

const rootElement = document.getElementById("root");

ReactDOM.render(
  <CookiesProvider>
    <App />
  </CookiesProvider>,
  rootElement
);

// Uncomment only in development
// module.hot.accept();

console.log(process.env.NODE_ENV);
