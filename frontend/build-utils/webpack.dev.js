const Dotenv = require("dotenv-webpack");
const webpack = require("webpack");

module.exports = {
  mode: "development",
  devtool: "eval-source-map",
  plugins: [
    new Dotenv({
      path: "./.env.development",
    }),
    new webpack.HotModuleReplacementPlugin(),
  ],
  devServer: {
    host: "localhost",
    compress: true,
    historyApiFallback: true,
    stats: "errors-only",
    hot: true,
  },
};
