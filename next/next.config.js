const withCSS = require('@zeit/next-css')
const withLess = require('@zeit/next-less')



// fix: prevents error when .css files are required by node
if (typeof require !== 'undefined') {
  // eslint-disable-next-line
  require.extensions['.css'] = (file) => {}
}


module.exports = withCSS(withLess({
  webpack(config, options) {
    // Further custom configuration here
    return config
  }
}))

