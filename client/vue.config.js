const path = require('path');

module.exports = {
  transpileDependencies: ['vuetify'],
  outputDir: path.resolve(__dirname, "../client/dist"),
  devServer: {
    proxy: "http://localhost:5000",
  },
};
