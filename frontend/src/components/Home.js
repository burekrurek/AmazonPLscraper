import React, { Component } from 'react'
import '../Home.css'


function AddItem(props) {
    function handleClick() {
        fetch('http://127.0.0.1:5000/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: props.value})
        })
        .then(response => response.json())
        .then(data => {
            alert('Server replied: ' + data.message)
        })
        .catch(error => {
            console.error('Error: ', error)
        })
    }
        return (
            <>
            <input type='text' placeholder='Start typing...' value={props.value} onChange={props.onChange}/>
            <button className='submitUrl' onClick={handleClick}>Submit</button>
            </>
        )
    }
class Home extends Component {
    handleChange = (event) => {
        this.setState({ inputValue: event.target.value })
    }
    constructor(props) {
        super(props)
        this.state = {
            rspn: [],
            inputValue : '',
            products: [],
            loading: true
        }
        this.fetchStatus = this.fetchStatus.bind(this)
    }
    componentDidMount() {
        this.fetchStatus()
        this.fetchProducts()
    }

    fetchStatus() {
        fetch('http://127.0.0.1:5000')
            .then(response => response.json())
            .then(r => {
                this.setState({
                    rspn: r
                })
            })
    }
    fetchProducts = () => {
        fetch('http://127.0.0.1:5000/get-products')
            .then(response => response.json())
            .then(data => {
                this.setState({ products: data.message || [], loading: false });
            })
            .catch(err => console.error('Error fetching products:', err))
    }

   
    render() {
        const { products, loading } = this.state;
        return ( < 
            div className = 'Home'> 
                {this.state.rspn.Status}
                <AddItem 
                    value={this.state.inputValue}
                    onChange={this.handleChange}
                />
                <h2>Products:</h2>
                <ul>
                {products.map((product, index) => (
                    <li key={index}>
                        {product[0]}
                    </li>
            ))}
                </ul>

             </div>
        )
    }
}
export default Home