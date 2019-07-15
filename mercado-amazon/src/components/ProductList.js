import React from 'react'
import { Product } from '.'
import Tabs from './ui/Tabs'

function ProductList(props) {
  const [ mlProducts, amznProducts ] = props.products

  return <>
    <Tabs titles={['Mercado Libre', 'Amazon']}>
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
    </Tabs>
  </>
}

export default ProductList
