module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      spacing:{
        "25vh" : "25vh",
        "50vh" : "50vh",
        "75vh" : "75vh",
      },
      borderRadius: {
        xl : "1.5rem"
      },
      fontWeight: ['hover', 'focus'],
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}