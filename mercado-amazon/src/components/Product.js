import React from 'react'
import MagnifyImg from 'react-image-magnify';

function Product(props) {
  const { product } = props
  return (
    <>
      <li>
        <div className="media product-tile">
          <div className="media-left">
            <figure className="image is-48x48">
            <MagnifyImg {...{
                  smallImage: {
                      alt: product.name,
                      isFluidWidth: true,
                      src: product.img,
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
      </li>
    </>
  )
}

export default Product
