// import { hot } from "react-hot-loader/root"; // Uncomment only in development
import React, { Component } from "react";
import { withCookies } from "react-cookie";
import "./style.scss";

class App extends Component {
  render() {
    return ("Test")
  }
}

export default withCookies(App);
// export default hot(withCookies(App));
