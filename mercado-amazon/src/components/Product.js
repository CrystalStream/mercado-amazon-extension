import React from 'react'

function Product(props) {
  const { product } = props

  return (
    <>
      <li>
        <img src={product.img} alt={product.name} />
        <p>{ product.name }</p>
        <span>{ product.price }</span>
      </li>
    </>
  )
}

export default Product
