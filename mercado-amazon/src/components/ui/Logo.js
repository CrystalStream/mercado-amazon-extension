import React from 'react'
import AmazonImg from '../../assets/img/amazon-logo.jpg'
import MLImg from '../../assets/img/ml-logo.jpg'

function Logo(props) {
  const { to, height, width }  = props

  switch(to) {
    case 'amazon':
      return <img src={AmazonImg} alt={to} height={height} width={width} />

    case 'ml':
      return <img src={MLImg} alt={to} height={height} width={width} />

    default:
      return to
  }
}

export default Logo
