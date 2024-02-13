# Reflection Week 8

### Summary 

This week's lectures explore methods to handle missing data and introduce concepts of recommendation systems (personalization, one of many important applications of machine learning and dimensionality reduction

### Concepts

* Handle missing data:

  * Skipping: dropping incomplete data rows or features.
    * Pros: flexible and easy to understand
    * Cons: might remove valuable data, "remove features or examples?", and might not benefit predictions if data is missing.
  * Sentinel values: replacing missing data with default values ("N/A", "missing"):
    * Pros: works well with categorical values and easy to understand.
    * Cons: might not work well with non-categorical if the features don't have clear sentinel values.
  * Imputation: using heuristic (self-learning) so the model can fill in missing data with better guesses for their values.
    * Two approaches:
      * Simple: use most popular terms (for categorical features) or mean/median (numerical).
      * Complex: use a learning algorithm to describe relationships between features (unsupervised learning).
    * Pros: can be applied to any model and used at prediction time.
    * Cons: may result in systematic errors and pose misunderstanding of original data if filled with the wrong value.
  * Modifying algorithm: using another model that is robust to the presence of missing data i.e. creating decision tree models whose branches handle missing data in some features.
    - Pros: can handle both categorical and numerical features and may have better accuracy.
    - Cons: computationally expensive (having to build another model), complex (what model to build)?

* Recommendation systems:

  * Output types:

    * Top k: returns similar choices with having the most identical feature values.

      Might be redundant because customers may like these already.

      How about other choices?

    * Diverse: return multi-faceted and "diverse" choices that might not be what customers really want.

      "Hedge our bets" and feed more data into the feedback loop if customers react and provide feedback on these choices.

  * Factors to concern in recommendation systems:

    * "Cold start":  concerns the issue that the system cannot draw any interference for users / items about which it has not yet gathered sufficient information.
    * Trends: models need to adapt to users (micro) and general trends (macro).
    * Scalability: needs to be efficient for a big number of users, and considers societal impact.

  * Methods of building recommendations:

    * Popularity: recommends whatever is universally popular
      * Pros: simple to understand and fast
      * Cons: no personalization and feedback loops
    * Learning classifiers: train classifiers to learn whether or not someone will like a recommendation
      * Pros: personalized and can capture context of the feedback (time, recent history), even when the user history is limited.
      * Cons: features may not be available or hard to work with, and may not perform well in practice compared to more sophisticated and modern models

* Dimensionality Reduction is the task of representing the data with fewer dimensions wile keeping meaningful relations between the data to help visualizing, easier learning, or saving saving space.

* Principle Component Analysis (PCA) is a popular dimensionality reduction algorithm that uses a linear projection from d-dimensional data to k-dimensional data (k<d)

  Algorithm Implementation:

### Concerns

* Why is it 