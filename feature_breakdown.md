# Feature Breakdown - AgriValue Agricultural Decision Support System

---

## 1. Mobile Application (Farmer)

**Goal:** Provide a simple mobile interface for farmers to enter farm details and receive market and residue-based recommendations.

### Implementation

- React Native + TypeScript Android application
- Farmer-friendly input interface
- Crop selection
- Produce quantity input
- Farm/location selection
- Selling date selection
- Recommendation dashboard
- Market comparison view
- Price forecast visualization
- Residue pathway comparison

### APIs

- `/recommend`
- `/forecast`
- `/markets`
- `/market-comparison`
- `/residue-pathways`

---

## 2. Farm & Crop Input Module

**Goal:** Collect the information required for market analysis, price forecasting, and residue valuation.

### Implementation

- Crop selection
- Produce quantity input
- Farm location input
- Selling date selection
- Input validation
- Required-field validation
- Invalid input handling

### Inputs

- Crop
- Quantity
- Location
- Selling date
- Crop grade/quality where applicable

---

## 3. Market Data Module

**Goal:** Provide historical agricultural market data required for price analysis and market comparison.

### Implementation

- Historical mandi price data
- Market-wise data filtering
- Crop-wise filtering
- Date-based filtering
- Data cleaning and validation
- Market data retrieval

### Data

- Market
- Commodity
- Date
- Minimum price
- Maximum price
- Modal price
- Arrivals where available

### APIs

- `/markets`
- `/market-data`
- `/market-comparison`

---

## 4. ML Price Forecasting Module (Core Engine)

**Goal:** Forecast expected crop prices for candidate markets using historical market data.

### Implementation

- Historical price preprocessing
- Time-based feature engineering
- Lag features
- Rolling statistics
- XGBoost regression model
- Market-wise price prediction
- Forecast validation

### Internal Components

- Data preprocessing
- Feature engineering
- Model inference
- Forecast generation
- Model evaluation

### APIs

- `/forecast`
- `/forecast/{crop}`
- `/ml/health`

---

## 5. Market & Economic Analysis Module

**Goal:** Compare candidate markets based on expected revenue after transportation costs.

### Implementation

- Forecasted price retrieval
- Gross revenue calculation
- Transportation cost estimation
- Net realization calculation
- Market-wise comparison
- Market ranking

### Calculations

```text
Expected Gross Revenue
= Forecasted Price × Produce Quantity

Expected Net Realization
= Expected Gross Revenue
  − Transportation Cost
  − Applicable Costs
```

---

## 6. Crop Residue Valuation Module

**Goal:** Estimate the economic value of crop residue and compare feasible residue utilization pathways.

### Implementation

- Residue quantity estimation
- Residue pathway identification
- Conversion factor application
- Output value estimation
- Processing and handling cost calculation
- Net residue value calculation
- Residue pathway comparison

### Calculation

```text
Net Residue Value
= Residue Quantity × Conversion Factor × Output Value
  − Processing/Handling Cost
```

### Outputs

- Estimated residue value
- Recommended residue pathway
- Alternative pathway comparison

---

## 7. Optimization & Recommendation Engine

**Goal:** Select a feasible market and residue pathway that maximize the farmer's expected total value.

### Implementation

- Market selection
- Residue pathway selection
- Net realization comparison
- Constraint handling
- Risk preference handling
- PuLP-based optimization
- Recommendation generation

### Objective

```text
Maximize Total Expected Value
= Net Produce Realization + Net Residue Value
```

### Constraints

- Produce quantity
- Residue quantity
- Market capacity
- Residue pathway capacity
- Transportation constraints
- Processing constraints
- User risk preference where applicable

### Output

- Recommended market
- Recommended residue pathway
- Expected net produce realization
- Expected residue value
- Total expected value

---

## 8. Explainability & Trust Module

**Goal:** Clearly explain why a particular market and residue pathway were recommended.

### Explanation Factors

- Forecasted market price
- Historical price trend
- Transportation cost
- Expected gross revenue
- Expected net realization
- Alternative market comparison
- Residue pathway value
- Processing/handling cost
- Key recommendation factors

### User Output

The application should present recommendations with supporting values rather than only showing a final recommendation.

---

## 9. Database Module

**Goal:** Store market data, forecasts, parameters, and recommendation results.

### Technology

- PostgreSQL

### Main Data

- Market information
- Historical prices
- Crop information
- Forecast results
- Transportation parameters
- Residue parameters
- Recommendation results

---

## 10. Backend API Module

**Goal:** Provide REST APIs connecting the React Native application with data processing, ML, optimization, and database components.

### Technology

- FastAPI
- Uvicorn

### Responsibilities

- Receive farmer inputs
- Validate requests
- Retrieve market data
- Run price forecasting
- Calculate economic values
- Run optimization
- Return recommendations
- Provide forecast and market comparison data

---

## 11. Data Processing Module

**Goal:** Prepare historical market data for analysis and machine learning.

### Technology

- Pandas
- NumPy

### Implementation

- Data cleaning
- Date processing
- Crop filtering
- Market filtering
- Missing-value handling
- Duplicate checking
- Feature creation
- Historical price preparation

---

## 12. Overall Feature Flow

```text
Farmer Input
     ↓
Farm & Crop Data
     ↓
Historical Market Data
     ↓
Price Forecasting
     ↓
Market & Economic Analysis
     ↓
Crop Residue Valuation
     ↓
Optimization Engine
     ↓
Recommendation
     ↓
Market + Residue Pathway + Expected Value
```

---

## 13. MVP Scope

The initial MVP focuses on:

- Karnataka region
- Five selected crops
- Historical market price analysis
- Market-wise price forecasting
- Transportation cost consideration
- Net produce realization
- Crop residue valuation
- Three selected residue pathways
- PuLP-based optimization
- Explainable recommendations
- React Native Android application
- FastAPI backend
- PostgreSQL database

---

## 14. Future Enhancements

The following features can be considered after the MVP:

- Real-time market prices
- Weather-aware forecasting
- Additional crops and markets
- Dynamic transportation distance and cost
- Price alerts
- Additional residue pathways
- Personalized farmer profiles
- Additional regional support