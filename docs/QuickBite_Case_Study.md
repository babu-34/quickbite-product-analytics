# QuickBite Product Analytics Case Study

## 1. Project Overview

QuickBite is a simulated B2C food-delivery product analytics project designed to analyze customer ordering behavior and identify opportunities to improve checkout and payment conversion.

The project combines SQL-based product analytics, MySQL data modeling, Power BI dashboarding, product discovery, and PRD development.

The analysis covers 20,000 orders and 254,129 user events across customers, restaurants, menu items, orders, order items, and product events.

The main objective was to identify where users drop off during the ordering journey, understand which user segments experience the greatest friction, and translate those findings into a measurable product improvement.

### Tools Used

* MySQL
* MySQL Workbench
* SQL
* Power BI
* Python
* Markdown
* Product Requirements Documentation (PRD)

### Product Focus

The analysis ultimately focuses on the checkout and payment experience, particularly for Android users.
## 2. Business Problem

QuickBite's simulated order data shows significant drop-off during the checkout and payment journey.

From 20,000 orders:

* **14,447 orders** were completed, giving an overall completion rate of **72.24%**.
* **2,706 orders** experienced payment failure, representing **13.53%** of all orders.
* **2,847 orders** were cancelled, representing **14.24%** of all orders.

Further segmentation showed a consistent device-level difference. Android users had a **70.52% completion rate** compared with **76.18% for iOS users**. Android also had a higher payment-failure rate of **14.61%**, compared with **11.05% for iOS**.

At the city and device level, **Pune Android** recorded the lowest completion rate at **68.88%**, followed by **Hyderabad Android at 69.24%**.

These results indicate that checkout and payment recovery are important areas for investigation, with Android users representing the primary target segment for the proposed experiment.

### Business Impact

Completed orders generated **₹25,732,359.03** in revenue, with an average order value of **₹1,781.16**.

A scenario analysis estimated that increasing the completion rate from **72.24% to 76%** could produce approximately **753 additional completed orders** at the same order volume. Using the current AOV, this corresponds to an estimated **₹13.41 lakh revenue opportunity**.

This is a scenario estimate based on the simulated dataset and should not be interpreted as a guaranteed production outcome.
## 3. Dataset & Tools

### Dataset

This project uses a **synthetic QuickBite food-delivery dataset** created for product analytics practice.

The database contains six main tables:

| Table         |    Rows | Purpose                               |
| ------------- | ------: | ------------------------------------- |
| `users`       |  10,000 | Customer information and segmentation |
| `restaurants` |     300 | Restaurant information                |
| `menu_items`  |   5,000 | Menu and item information             |
| `orders`      |  20,000 | Order transactions and outcomes       |
| `order_items` |  49,961 | Items included in orders              |
| `events`      | 254,129 | User behavior and funnel events       |

### Key Dimensions

The analysis uses dimensions including:

* Device type
* City
* Payment method
* Order status
* User behavior events

### Technology Stack

**Python**

* Used to generate the synthetic dataset and prepare CSV files.

**MySQL**

* Used to store the data and perform product analytics queries.
* SQL views were created specifically for dashboard reporting.

**MySQL Workbench**

* Used for database management, SQL analysis, and validation.

**Power BI**

* Used to build the interactive product analytics dashboard.

**Markdown**

* Used to document the Product Brief, PRD, and case study.

### Dashboard SQL Views

Five core dashboard views were created during the analysis:

```text
dashboard_kpis
dashboard_funnel
dashboard_device
dashboard_city_device
dashboard_payment_method
dashboard_order_status
```

These views separate analytical logic from visualization and make the Power BI dashboard easier to maintain.

### Data Limitation

Because the dataset is synthetic, the findings represent a **portfolio case study and analytical hypothesis**, not actual QuickBite production performance.
## 4. SQL Analysis & Key Findings

SQL was used to analyze the order funnel, order outcomes, device performance, city-level performance, and payment methods.

### 4.1 Order Funnel Analysis

The event funnel showed the following progression:

| Funnel Stage    | Events |
| --------------- | -----: |
| App Open        | 50,000 |
| Restaurant View | 50,000 |
| Item View       | 50,000 |
| Add to Cart     | 35,079 |
| Checkout Start  | 30,214 |
| Payment Attempt | 24,389 |
| Order Completed | 14,447 |

The largest relative drop-off in the final stages occurred between **Payment Attempt and Order Completed**. Only 14,447 of 24,389 payment attempts resulted in completed orders, which corresponds to a conversion of approximately **59.24%** from that stage.

This suggested that checkout and payment recovery warranted deeper investigation.

### 4.2 Overall Order Performance

The order-level analysis showed:

| Metric               | Result |
| -------------------- | -----: |
| Total Orders         | 20,000 |
| Completed Orders     | 14,447 |
| Payment Failed       |  2,706 |
| Cancelled            |  2,847 |
| Completion Rate      | 72.24% |
| Payment Failure Rate | 13.53% |
| Cancellation Rate    | 14.24% |

### 4.3 Device Analysis

Device segmentation showed a clear difference between Android and iOS:

| Device  | Completion Rate | Payment Failure Rate | Cancellation Rate |
| ------- | --------------: | -------------------: | ----------------: |
| Android |          70.52% |               14.61% |            14.87% |
| iOS     |          76.18% |               11.05% |            12.77% |

Android completion was **5.66 percentage points lower** than iOS, while Android payment failure was **3.56 percentage points higher**.

This made Android the primary segment for the proposed product experiment.

### 4.4 City + Device Segmentation

The combined city and device analysis identified several low-completion segments.

| City      | Device  | Completion Rate | Payment Failure Rate | Cancellation Rate |
| --------- | ------- | --------------: | -------------------: | ----------------: |
| Pune      | Android |          68.88% |               14.72% |            16.40% |
| Hyderabad | Android |          69.24% |               15.60% |            15.16% |
| Chennai   | Android |          70.64% |               15.62% |            13.74% |
| Mumbai    | Android |          70.77% |               14.33% |            14.90% |

Pune Android recorded the lowest observed completion rate at **68.88%**. Hyderabad Android also showed a relatively low completion rate of **69.24%** alongside a **15.60% payment-failure rate**.

### 4.5 Payment Method Analysis

Payment-method performance was comparatively close:

| Payment Method | Completion Rate | Payment Failure Rate | Cancellation Rate |
| -------------- | --------------: | -------------------: | ----------------: |
| Wallet         |          71.95% |               13.85% |            14.19% |
| Cash           |          72.36% |               13.68% |            13.96% |
| Card           |          72.66% |               13.68% |            13.66% |
| UPI            |          71.98% |               12.90% |            15.12% |

The relatively narrow differences across payment methods suggested that the product opportunity should not be framed as a problem with one individual payment method.

### 4.6 Revenue Analysis

Completed orders generated:

* **Completed Orders:** 14,447
* **Revenue:** ₹25,732,359.03
* **Average Order Value:** ₹1,781.16

A scenario analysis showed that increasing completion from **72.24% to 76%** at the same order volume would result in approximately **753 additional completed orders**.

At the current AOV, that corresponds to approximately **₹13.41 lakh** in additional revenue opportunity.

This is a scenario estimate based on the synthetic dataset, not a guaranteed business outcome.

### 4.7 Analytical Conclusion

The SQL analysis moved the investigation through several levels:

```text
Overall Performance
        ↓
Funnel Drop-off
        ↓
Device Segmentation
        ↓
City + Device Segmentation
        ↓
Payment Method Analysis
        ↓
Business Impact
```

The combined evidence led to the product hypothesis that improving **payment recovery and checkout friction for Android users** could increase successful order completion.

The analysis identifies a correlation and an opportunity for experimentation; it does not establish that Android technology itself is the root cause of the observed failures.
## 5. Power BI Dashboard

Power BI was used to convert the SQL analysis into an interactive product analytics dashboard.

The dashboard was designed as a single-page executive view so that a product manager or interviewer can understand the main business problem quickly.

### 5.1 KPI Summary

The dashboard presents five primary KPIs:

| KPI                   |   Value |
| --------------------- | ------: |
| Total Orders          |     20K |
| Order Completion Rate |  72.24% |
| Payment Failure Rate  |  13.53% |
| Cancellation Rate     |  14.24% |
| Completed Revenue     | ₹25.73M |

These KPIs provide an immediate view of order volume, conversion, major failure points, and business value.

### 5.2 Order Funnel

The funnel visual shows the customer journey from app opening through order completion:

```text
App Open
   ↓
Restaurant View
   ↓
Item View
   ↓
Add to Cart
   ↓
Checkout Start
   ↓
Payment Attempt
   ↓
Order Completed
```

This visual helps identify where users are being lost during the ordering process.

### 5.3 Android vs iOS Performance

The device-performance visual compares completion and payment-failure rates between Android and iOS.

| Device  | Completion Rate | Payment Failure Rate |
| ------- | --------------: | -------------------: |
| Android |          70.52% |               14.61% |
| iOS     |          76.18% |               11.05% |

This view highlights the device-level difference that motivated the Android-focused product hypothesis.

### 5.4 City + Device Performance

The city/device visual allows performance to be examined across individual segments.

The lowest observed completion rates were:

| Segment             | Completion Rate |
| ------------------- | --------------: |
| Pune — Android      |          68.88% |
| Hyderabad — Android |          69.24% |

This segmentation helps identify where the checkout problem appears most strongly in the simulated dataset.

### 5.5 Order Status Breakdown

The dashboard shows the composition of all orders:

* Completed: **72.24%**
* Cancelled: **14.24%**
* Payment Failed: **13.53%**

This allows the viewer to distinguish successful orders from the two major unsuccessful outcomes.

### 5.6 Payment Method Analysis

The payment-method visual compares payment-failure rates across Wallet, Cash, Card, and UPI.

The observed payment-failure rates ranged from **12.90% to 13.85%**, indicating relatively small differences between payment methods.

This supported focusing the product hypothesis on the broader checkout and payment-recovery experience rather than a single payment method.

### 5.7 Dashboard Design Principles

The dashboard was designed around:

* Clear KPI hierarchy
* Consistent card and chart sizing
* Minimal visual clutter
* Consistent percentage formatting
* Logical left-to-right and top-to-bottom information flow
* Interactive device and city filtering
* Direct connection between analytical findings and product decisions

### 5.8 Dashboard Outcome

The dashboard turns multiple SQL analyses into a single decision-support view:

```text
Business Metrics
       ↓
Funnel Performance
       ↓
Device Comparison
       ↓
City + Device Segmentation
       ↓
Order Outcome Analysis
       ↓
Payment Method Analysis
```

The dashboard therefore acts as the analytical evidence layer for the proposed product improvement.
## 6. Product Insight & Hypothesis

### 6.1 Product Insight

The analysis shows that the main opportunity is concentrated around the checkout and payment stage rather than a single payment method.

The order funnel shows a substantial drop between payment attempts and completed orders. Device-level analysis also shows that Android users have a lower completion rate and a higher payment-failure rate than iOS users.

The city and device analysis provides additional evidence that some Android segments experience weaker performance. Pune Android has a 68.88% completion rate, while Hyderabad Android has a 69.24% completion rate and a 15.60% payment-failure rate.

Payment-method performance is comparatively close across Wallet, Cash, Card, and UPI, so the evidence does not point to one payment method as the primary issue.

### 6.2 Product Opportunity

The opportunity is to make a failed payment a **recoverable checkout state** rather than an endpoint that forces the user to restart the process.

The product should reduce the effort required to recover from payment failure while preserving the user's progress.

### 6.3 Product Hypothesis

**If** Android users receive a simpler payment-recovery experience with a clear failure message, one-tap retry, preserved cart and checkout details, and alternative payment methods,

**then** order completion should increase and payment-related drop-offs should decrease,

**because** users can recover from failed payments without rebuilding their order.

### 6.4 Proposed Feature

**Smart Payment Recovery**

The feature includes:

1. Clear payment-failure messaging
2. One-tap payment retry
3. Cart and checkout preservation
4. Alternative payment methods
5. Clear payment-processing status
6. Duplicate-payment and duplicate-order protection

### 6.5 Target Segment

The initial product experiment targets eligible **Android users reaching the checkout/payment stage**.

The Android focus is based on observed differences in the simulated dataset and should be validated with production data before any real product decision.

### 6.6 Expected Product Impact

The feature is designed to improve:

* Order Completion Rate
* Payment Recovery Rate
* Checkout-to-Order Conversion

while monitoring:

* Payment Failure Rate
* Cancellation Rate
* Refund Rate
* Duplicate Payment Attempts
* Customer Complaints

### 6.7 Experiment Baseline

Current overall baseline:

**Order Completion Rate:** 72.24%

Proposed experiment target:

**76% or higher**

The target is a proposed hypothesis-testing goal and is not an observed result.

### 6.8 Analytical-to-Product Decision Flow

```text id="u4ih0s"
SQL Analysis
     ↓
Identify Funnel Drop-off
     ↓
Segment by Device
     ↓
Segment by City + Device
     ↓
Check Payment Methods
     ↓
Identify Checkout/Payment Recovery Opportunity
     ↓
Smart Payment Recovery Hypothesis
     ↓
A/B Experiment
```
## 7. Smart Payment Recovery — Feature Design

### 7.1 Feature Overview

Smart Payment Recovery is a proposed checkout feature designed to help users recover from unsuccessful payment attempts without restarting their food order.

The feature focuses on reducing payment-related friction while preserving the user's progress.

### 7.2 Proposed User Experience

```text
Checkout
   ↓
Payment Attempt
   ↓
Payment Failed
   ↓
Clear Failure Message
   ↓
┌───────────────────────────────┐
│ Retry Payment                 │
│ Change Payment Method         │
│ View Payment Status           │
└───────────────────────────────┘
   ↓
Successful Payment
   ↓
Order Confirmation
```

### 7.3 Core Features

**Clear Failure Message**

Instead of displaying a generic error, the user receives a clear message explaining that the payment was unsuccessful and that the order information is still available.

**One-Tap Retry**

A prominent retry action allows the user to attempt payment again without restarting checkout.

**Cart Preservation**

The selected food items, quantities, restaurant, and checkout information remain available after a failed payment.

**Alternative Payment Methods**

Users can switch to another available payment method without rebuilding the order.

**Payment Status**

The experience clearly distinguishes between successful, failed, and processing payments.

**Duplicate Transaction Protection**

The backend verifies payment and order state before confirming an order, reducing the risk of duplicate transactions.

### 7.4 User Story

> As an Android QuickBite customer whose payment failed, I want to retry or change my payment method without rebuilding my order so that I can complete my purchase with minimal effort.

### 7.5 Analytics Events

The feature should track:

| Event                    | Purpose                          |
| ------------------------ | -------------------------------- |
| `payment_failed`         | Identify failed payments         |
| `payment_retry_clicked`  | Measure retry intent             |
| `payment_method_changed` | Measure alternative-method usage |
| `payment_recovered`      | Measure successful recovery      |
| `checkout_abandoned`     | Measure unsuccessful recovery    |
| `order_completed`        | Measure final conversion         |

### 7.6 Product Success

The feature should be evaluated based on its effect on:

**Primary metric**

* Order Completion Rate

**Secondary metrics**

* Payment Recovery Rate
* Payment Failure Rate
* Checkout-to-Order Conversion
* Average Order Value

**Guardrails**

* Cancellation Rate
* Refund Rate
* Duplicate Payment Attempts
* Customer Complaints
* Payment Processing Time

### 7.7 Why This Feature Was Selected

The feature was selected because the analysis showed:

```text
Payment Attempt
      ↓
Large drop-off
      ↓
Lower Android completion
      ↓
Higher Android payment failure
      ↓
Opportunity for payment recovery
```

The proposed feature therefore directly addresses the identified checkout friction while allowing its impact to be tested quantitatively.
## 8. Experiment Results Framework & Business Impact

### 8.1 Experiment Design

The Smart Payment Recovery feature would be evaluated using a randomized A/B experiment among eligible Android users who reach the checkout and payment stage.

| Group     | Experience                           |
| --------- | ------------------------------------ |
| Control   | Existing checkout/payment experience |
| Treatment | Smart Payment Recovery               |

Users should be randomly assigned to the two groups, with a consistent assignment throughout the experiment.

### 8.2 Primary Metric

**Order Completion Rate**

Current overall baseline:

**72.24%**

Proposed target:

**76% or higher**

The target is a hypothesis-testing goal, not an expected or guaranteed result.

### 8.3 Secondary Metrics

The experiment should measure:

* Payment Recovery Rate
* Payment Failure Rate
* Checkout-to-Order Conversion Rate
* Cancellation Rate
* Average Order Value
* Additional Completed Orders

### 8.4 Guardrail Metrics

The feature should also be monitored for unintended effects:

* Refund Rate
* Duplicate Payment Attempts
* Customer Complaints
* Payment Processing Time
* Cancellation Rate

An improvement in conversion should not be considered sufficient by itself if important guardrail metrics deteriorate.

### 8.5 Statistical Evaluation

The experiment results should be evaluated using an appropriate statistical significance test for the primary conversion metric.

The analysis should report:

* Control conversion rate
* Treatment conversion rate
* Absolute difference
* Relative change
* Confidence interval
* Statistical significance
* Sample size

The experiment should also be checked for data-quality issues, uneven group allocation, and unexpected changes in traffic or payment behavior.

### 8.6 Business Opportunity Scenario

The existing dataset contains:

**20,000 total orders**

and:

**14,447 completed orders**

At a hypothetical **76% completion rate**, the same order volume would correspond to:

**15,200 completed orders**

That represents:

**753 additional completed orders**

Using the current average order value of **₹1,781.16**, the estimated incremental revenue opportunity is approximately:

**₹13.41 lakh**

This is a scenario calculation based on the synthetic dataset and current AOV. It does not represent a forecast or guaranteed business result.

### 8.7 Hypothetical Result Interpretation Framework

If the experiment produces:

**Higher completion + lower payment failure + stable guardrails**

the product team would have evidence supporting further rollout.

If completion improves but guardrail metrics deteriorate, the team should investigate the trade-off before expanding the feature.

If there is no meaningful improvement, the hypothesis should be reconsidered and the payment-recovery experience investigated further.

### 8.8 Measurement Flow

```text
Control vs Treatment
        ↓
Order Completion
        ↓
Payment Recovery
        ↓
Payment Failure
        ↓
Cancellation + Guardrails
        ↓
Statistical Evaluation
        ↓
Rollout Decision
```

The purpose of the experiment is to replace assumptions about product impact with measurable evidence.
## 9. Limitations & Learnings

### 9.1 Project Limitations

**Synthetic Dataset**

The QuickBite dataset is simulated for portfolio and learning purposes. The observed customer behavior, payment failures, and conversion rates may not represent real food-delivery users.

**Limited Root-Cause Information**

The available dataset shows payment outcomes but does not contain detailed payment-gateway error codes, network conditions, device models, app versions, or technical logs. Therefore, the analysis identifies an opportunity but does not prove the technical root cause of payment failures.

**No Actual Experiment Results**

The Smart Payment Recovery feature is a proposed product concept. No real A/B test was conducted, so the 76% completion target and ₹13.41 lakh opportunity are scenario calculations rather than measured improvements.

**Limited Time Dimension**

The analysis primarily focuses on aggregated performance. Additional time-based analysis would be useful for identifying weekday/weekend patterns, seasonal effects, and changes in payment performance.

### 9.2 Key Learnings

This project helped demonstrate an end-to-end product analytics workflow:

```text id="h5q2b1"
Business Problem
      ↓
Data Exploration
      ↓
SQL Analysis
      ↓
Segmentation
      ↓
Dashboard
      ↓
Product Insight
      ↓
Feature Hypothesis
      ↓
Experiment Design
      ↓
Business Impact
```

### 9.3 Technical Learnings

* Built and queried a MySQL product analytics database.
* Created reusable SQL views for dashboard reporting.
* Used SQL aggregation, conditional logic, joins, grouping, and segmentation.
* Connected MySQL to Power BI.
* Built KPI cards and analytical dashboard visuals.
* Used Power BI formatting, filtering, and dashboard layout techniques.

### 9.4 Product Analytics Learnings

* Funnel analysis helps identify where users drop out of a journey.
* Segmentation can reveal problems hidden by overall averages.
* Business impact should be connected to measurable product metrics.
* A product hypothesis should be testable rather than presented as a fact.
* Guardrail metrics are necessary when optimizing conversion.
* Synthetic data requires clear communication of assumptions and limitations.

### 9.5 Product Thinking Learning

The most important learning from this project was the transition from **“What does the data show?”** to **“What product problem should we investigate next?”**

The analysis did not simply identify a low-performing metric. It connected funnel behavior, device segmentation, city-level performance, payment outcomes, and business impact to form a testable product hypothesis.

That approach makes the project more representative of a real Product Analyst workflow.
## 10. Final Takeaway

This project demonstrates an end-to-end Product Analytics workflow using a simulated food-delivery product.

The analysis started with a broad question: **Where are users dropping off during the ordering journey?**

SQL analysis of the QuickBite dataset identified a 72.24% overall order completion rate and a significant drop between payment attempts and completed orders. Further segmentation showed that Android users had a lower completion rate and higher payment-failure rate than iOS users. City-level analysis highlighted Pune Android and Hyderabad Android as segments with lower observed completion rates.

The analysis then translated these findings into a product opportunity:

**Smart Payment Recovery**

The proposed feature helps users recover from failed payments through clear failure messaging, one-tap retry, preserved cart and checkout information, alternative payment methods, and duplicate-transaction protection.

The feature would be validated through an A/B experiment using **Order Completion Rate** as the primary metric and payment recovery, payment failure, cancellation, and other guardrail metrics as supporting measures.

A scenario analysis estimated that moving completion from 72.24% to 76% at the same order volume would correspond to approximately **753 additional completed orders** and about **₹13.41 lakh of additional revenue opportunity** based on the current AOV.

The project demonstrates the ability to move from:

```text
Data
  ↓
SQL Analysis
  ↓
Dashboard
  ↓
Insight
  ↓
Product Hypothesis
  ↓
PRD
  ↓
Experiment Design
  ↓
Business Impact
```

The key takeaway is that effective Product Analytics is not only about finding numbers. It is about turning evidence into a clear product problem, defining a testable solution, and establishing how success will be measured.
