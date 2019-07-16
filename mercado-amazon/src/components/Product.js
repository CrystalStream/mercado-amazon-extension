import React from 'react'

function Product(props) {
  const { product } = props
  return (
    <>
      <li>
        <div className="media product-tile">
          <div className="media-left">
            <figure className="image is-48x48">
              <img src={product.img} alt={product.name} />
            </figure>
          </div>
          <div className="media-content">
            <p className="title is-5">{product.name}</p>
            <p className="subtitle is-6 has-text-danger">{product.price}</p>
          </div>
        </div>
      </li>
    </>
  )
}

export default Product
