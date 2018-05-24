const path = require("path");
const webpack = require("webpack");
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

const BUILD_DIR = path.resolve(__dirname, '../build');
const CLIENT_DIR = path.resolve(__dirname, '../src/client');
const TEMPLATES_DIR = path.resolve(CLIENT_DIR, 'templates');
const ASSETS_DIR = path.resolve(CLIENT_DIR, 'assets');
const NODE_DIR = path.resolve(__dirname, '../node_modules');

const webpackConfig = {
  mode: 'development',
  entry: {
    app: [
        path.join(NODE_DIR, 'bootstrap/dist/js/bootstrap.js'),
        path.join(CLIENT_DIR, 'index.js'),
        path.join(ASSETS_DIR, 'css/app.css'),
        path.join(ASSETS_DIR, 'css/styles.css')
    ]
  },
  output: {
      path: BUILD_DIR,
      publicPath: '/build/',
      filename: '[name][hash]_bundle.js'
  },
  module: {
         rules: [
             {
                 test: /\.js$/,
                 loader: 'babel-loader',
                 query: {
                     presets: ['es2015']
                 }
             },
             {
                 test: /\.vue$/,
                 loader: 'vue-loader'
             },
             {
                test:/\.css$/,
                use:['style-loader','css-loader']
             }
         ]
     },
     plugins: [
         new webpack.NamedModulesPlugin(),
         new webpack.HotModuleReplacementPlugin(),
         new CleanWebpackPlugin(
             [BUILD_DIR],
             {
                 root: __dirname,
                 watch: true,
                 allowExternal: true,
                 exclude: ['index.html']
             }
         ),
         new webpack.ProvidePlugin({
             jQuery: 'jquery',
             $: 'jquery',
             jquery: 'jquery',
             "window.jquery": 'jquery',
             "window.jQuery": 'jquery',
             "window.$": 'jquery',
             Popper: ['popper.js', 'default'],
         }),
         new HtmlWebpackPlugin({
             title: 'Welcome to the App',
             template: path.join(TEMPLATES_DIR, 'layout.html'),
             filename: 'index.html'
         })
     ],
     stats: {
         colors: true
     },
     devtool: 'source-map',
     devServer: {
       contentBase: BUILD_DIR,
       hot: true
     },
     optimization: {
     minimizer: [
      new UglifyJsPlugin({
        cache: true,
        parallel: true,
        uglifyOptions: {
          compress: true,
          ecma: 6,
          mangle: true
        },
        sourceMap: true
      })
     ]
    }
};

module.exports = webpackConfig;