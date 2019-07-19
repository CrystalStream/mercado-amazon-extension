import React from 'react'
import MagnifyImg from 'react-image-magnify';
import utils from '../utils'

function Product(props) {
  const { product } = props
  return (
    <>
      <li>
        <a onClick={() => { utils.openTab(product.url) }}>
          <div className="media product-tile">
            <div className="media-left">
              <figure className="image is-64x64">
              <MagnifyImg {...{
                    imageClassName: 'product-img',
                    smallImage: {
                        alt: product.name,
                        src: product.img,
                        width: 70,
                        height: 85
                    },
                    largeImage: {
                        src: product.img,
                        alt: product.name,
                        width: 260,
                        height: 345
                    },
                    enlargedImagePortalId: 'portal',
                    enlargedImageContainerDimensions: {
                        width: 260,
                        height: 345
                    }
                }} />
              </figure>
            </div>
            <div className="media-content">
              <p className="title is-5">{product.name}</p>
              <p className="subtitle is-6 has-text-danger">{product.price}</p>
            </div>
          </div>
        </a>
      </li>
    </>
  )
}

export default Product
