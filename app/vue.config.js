const path = require('path');

module.exports = {
  transpileDependencies: ['vuetify'],
  outputDir: 'dist',
  devServer: {
    proxy: "http://localhost:5000",
  },
};
