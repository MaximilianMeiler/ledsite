import React from 'react'

const Box = ({red, green, blue}) => {
  return (
    <div className='displayBox' style={{backgroundColor: 'rgba(' + red + ',' + green + "," + blue + ')'}}></div>
  )
}

export default Box