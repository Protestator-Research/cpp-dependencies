#include <mlpack/methods/random_forest.hpp>

using namespace mlpack;

int main()
{
    const size_t numClasses = 2;
    const size_t minimumLeafSize = 5;
    const size_t numTrees = 10;

    // Training on an empty dataset trips armadillo's argument checks in Debug builds.
    const size_t numPoints = 50;
    arma::mat dataset(4, numPoints, arma::fill::randu);
    arma::Row<size_t> labels(numPoints), predictions;
    for (size_t i = 0; i < numPoints; ++i)
        labels[i] = i % numClasses;
    RandomForest<GiniGain, RandomDimensionSelect> rf(dataset, labels, numClasses, numTrees, minimumLeafSize);
    rf.Classify(dataset, predictions);
}
