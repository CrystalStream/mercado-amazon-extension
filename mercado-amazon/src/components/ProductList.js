import React, { useState } from 'react'
import { Product } from '.'
import Tabs from './ui/Tabs'
import Logo from './ui/Logo'

function ProductList(props) {
  const [ mlProducts, amznProducts ] = props.products
  const [ selectedIndex, setSelected ] = useState(0)
  const titles = [
    <Logo to="ml" height="40" width="40" />,
    <Logo to="amazon" height="70" width="70" />
  ]

  return <>
    <Tabs titles={titles} selectedIndex={selectedIndex} onClick={setSelected}>
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
