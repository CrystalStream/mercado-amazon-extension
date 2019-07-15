import React from 'react'
import { Product } from '.'

function ProductList(props) {
  const [ mlProducts, amznProducts ] = props.products

  return <>
    <ul>
      {
        mlProducts && mlProducts.map((e, i) => {
          return <Product key={i} product={e}/>
        })
      }
    </ul>
    <ul>
      {
        amznProducts && amznProducts.map((e, i) => {
          return <Product key={i} product={e}/>
        })
      }
    </ul>
  </>
}

export default ProductList
