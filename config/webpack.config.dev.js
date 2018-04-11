const path = require("path");
const webpack = require("wepack");

const config = {
  entry: './client/index.js',
  output: {
      path: path.resolve(__dirname, 'build'),
      filename: 'app.bundle.js'
  },
    module: {
         rules: [
             {
                 test: /\.js$/,
                 loader: 'babel-loader',
                 query: {
                     presets: ['es2015']
                 }
             }
         ]
     },
     stats: {
         colors: true
     },
     devtool: 'source-map'
};

module.exports = config;