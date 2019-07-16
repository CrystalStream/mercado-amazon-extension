import React from 'react'
import { Product } from '.'
import Tabs from './ui/Tabs'

function ProductList(props) {
  const [ mlProducts, amznProducts ] = props.products

  return <>
    <Tabs titles={['Mercado Libre', 'Amazon']}>
      <div className="ml-container">
        <ul>
          {
            mlProducts && mlProducts.map((e, i) => {
              return <Product key={i} product={e}/>
            })
          }
        </ul>
      </div>
    </Tabs>
  </>
}

export default ProductList
