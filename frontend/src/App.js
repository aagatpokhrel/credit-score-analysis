import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState(1);
  const [fullName, setFullName] = useState('');
  const [dateOfBirth, setDateOfBirth] = useState('');
  const [seniority, setSeniority] = useState(0);
  const [isHomeOwner, setIsHomeOwner] = useState(false);
  const [address, setAddress] = useState('');
  const [maritalStatus, setMaritalStatus] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [ssn, setSSN] = useState('');
  const [expenses, setExpenses] = useState(0);
  const [income, setIncome] = useState(0);
  const [assets, setAssets] = useState(0);
  const [debt, setDebt] = useState(0);
  const [loanTaken, setLoanTaken] = useState(0);
  const [paidBeforeDeadline, setPaidBeforeDeadline] = useState(0);
  const [averageOverdueTime, setAverageOverdueTime] = useState(0);

  const handleFullNameChange = (event) => {
    setFullName(event.target.value);
  };

  const handleDateOfBirthChange = (event) => {
    setDateOfBirth(event.target.value);
  };

  const handleSeniorityChange = (event) => {
    setSeniority(parseInt(event.target.value));
  };

  const handleHomeOwnerChange = (event) => {
    setIsHomeOwner(event.target.value === 'true');
  };

  const handleAddressChange = (event) => {
    setAddress(event.target.value);
  };

  const handleMaritalStatusChange = (event) => {
    setMaritalStatus(event.target.value);
  };

  const handlePhoneNumberChange = (event) => {
    setPhoneNumber(event.target.value);
  };

  const handleSSNChange = (event) => {
    setSSN(event.target.value);
  };

  const handleExpensesChange = (event) => {
    setExpenses(parseInt(event.target.value));
  };

  const handleIncomeChange = (event) => {
    setIncome(parseInt(event.target.value));
  };

  const handleAssetsChange = (event) => {
    setAssets(parseInt(event.target.value));
  };

  const handleDebtChange = (event) => {
    setDebt(parseInt(event.target.value));
  };

  const handleLoanTakenChange = (event) => {
    setLoanTaken(parseInt(event.target.value));
  };

  const handlePaidBeforeDeadlineChange = (event) => {
    setPaidBeforeDeadline(parseInt(event.target.value));
  };

  const handleAverageOverdueTimeChange = (event) => {
    setAverageOverdueTime(parseInt(event.target.value));
  };

  const handleNext = () => {
    setActiveTab((prevTab) => prevTab + 1);
  };

  const handleResponse = (data) => {
    // Access the score and report card from the response data
    const score_ = data.score;
    const report = data.report;
    
    const reportContainer = document.getElementById('report');

    // Create a card element
    const reportCard = document.createElement('div');
    reportCard.className = 'card';

    // Extract the report data
    const { name, address, score, seniority, age } = report;

    // Create HTML content for the report card
    const reportContent = `
      <h2>Report</h2>
      <p><strong>Name:</strong> ${name}</p>
      <p><strong>Address:</strong> ${address}</p>
      <p><strong>Score:</strong> ${score_}</p>
      <p><strong>Seniority:</strong> ${seniority}</p>
      <p><strong>Age:</strong> ${age}</p>
    `;

    // Set the HTML content of the report card
    reportCard.innerHTML = reportContent;

    // Clear any previous content in the report container
    reportContainer.innerHTML = '';

    // Append the report card to the report container
    reportContainer.appendChild(reportCard);
    // Update the DOM to display the score and report card
    document.getElementById('score').innerText = `Score: ${score}`;
    // document.getElementById('report').innerText = `Report: ${JSON.stringify(report)}`;
  }
  
  const handleSearch = (event) => {
    event.preventDefault();
    const searchQuery = event.target.elements.query.value;
    axios
      .get(`http://localhost:5000/search?query=${searchQuery}`)
      .then((response) => {
        console.log(response.data); // handle the search results
        handleResponse(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  
  const handleSubmit = (event) => {
    event.preventDefault();
  
    axios
      .post('http://localhost:5000/credit-score', {
        fullName,
        dateOfBirth,
        seniority,
        isHomeOwner,
        address,
        maritalStatus,
        phoneNumber,
        ssn,
        expenses,
        income,
        assets,
        debt,
        loanTaken,
        paidBeforeDeadline,
        averageOverdueTime,
      })
      .then((response) => {
        console.log(response.data);
        handleResponse(response.data); // handle the response from the backend
      })
      .catch((error) => {
        console.error(error);
      });
  };
  
  return (
    <div className="App">
      <header>
        <nav>
          <div className="search-container">
            <form onSubmit={handleSearch}>
              <input type="text" name="query" placeholder="Search SSN" />
              <button type="submit" class="button search">Generate</button>
            </form>
          </div>
        </nav>
      </header>
      <div className="tab-container">
        <div
          className={`tab ${activeTab === 1 ? 'active' : ''}`}
          onClick={() => setActiveTab(1)}
          >
          Personal Details
        </div>
        <div
          className={`tab ${activeTab === 2 ? 'active' : ''}`}
          onClick={() => setActiveTab(2)}
          >
          Financial Details
        </div>
      </div>
      <div>
        {activeTab === 1 && (
          <div className="form-container">
            <h2>Personal Details</h2>
            <form onSubmit={handleNext}>
              <div className="form-group">
                <label>Full Name</label>
                <input
                  type="text"
                  value={fullName}
                  onChange={handleFullNameChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Date of Birth</label>
                <input
                  type="date"
                  value={dateOfBirth}
                  onChange={handleDateOfBirthChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Seniority (Employed Years)</label>
                <input
                  type="number"
                  value={seniority}
                  onChange={handleSeniorityChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Home Owner</label>
                <select value={isHomeOwner} onChange={handleHomeOwnerChange} required>
                  <option value={true}>Yes</option>
                  <option value={false}>No</option>
                </select>
              </div>
              <div className="form-group">
                <label>Address</label>
                <input
                  type="text"
                  value={address}
                  onChange={handleAddressChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Marital Status</label>
                <div className="radio-group">
                  <div className="radio-option">
                    <input
                      type="radio"
                      id="single"
                      name="maritalStatus"
                      value="single"
                      checked={maritalStatus === 'single'}
                      onChange={handleMaritalStatusChange}
                    />
                    <label htmlFor="single">Single</label>
                  </div>
                  <div className="radio-option">
                    <input
                      type="radio"
                      id="married"
                      name="maritalStatus"
                      value="married"
                      checked={maritalStatus === 'married'}
                      onChange={handleMaritalStatusChange}
                    />
                    <label htmlFor="married">Married</label>
                  </div>
                </div>
              </div>
              <div className="form-group">
                <label>Phone Number</label>
                <input
                  type="text"
                  value={phoneNumber}
                  onChange={handlePhoneNumberChange}
                  required
                />
              </div>
              <div className="form-group">
                <button type="submit" className="button next">
                  Next
                </button>
              </div>
            </form>
          </div>
        )}
      
        {activeTab === 2 && (
          <div className="form-container">
            <h2>Financial Details</h2>
            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <label>SSN (Social Security Number)</label>
                <input
                  type="text"
                  value={ssn}
                  onChange={handleSSNChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Expenses (in K)</label>
                <input
                  type="number"
                  value={expenses}
                  onChange={handleExpensesChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Income</label>
                <input
                  type="number"
                  value={income}
                  onChange={handleIncomeChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Assets</label>
                <input
                  type="number"
                  value={assets}
                  onChange={handleAssetsChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Debt</label>
                <input
                  type="number"
                  value={debt}
                  onChange={handleDebtChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Times Loan Taken</label>
                <input
                  type="number"
                  value={loanTaken}
                  onChange={handleLoanTakenChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>No. of Times Paid Before Deadline</label>
                <input
                  type="number"
                  value={paidBeforeDeadline}
                  onChange={handlePaidBeforeDeadlineChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Average Overdue Time (in days)</label>
                <input
                  type="number"
                  value={averageOverdueTime}
                  onChange={handleAverageOverdueTimeChange}
                  required
                />
              </div>
              <div className="form-group">
                <button type="submit" className="button submit">
                  Submit
                </button>
              </div>
            </form>
          </div>
        )}
        </div>
        <div className='other-container'>
          <p id="score"></p>
          <div id="report"></div>
        </div>
      </div>
  );
}

export default App;