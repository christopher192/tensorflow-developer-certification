from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def performance_metrics(y_true, y_pred):
  model_accuracy = accuracy_score(y_true, y_pred) * 100
  model_precision, model_recall, model_f1, _ = precision_recall_fscore_support(y_true, y_pred, average = "weighted")
  model_results = { "accuracy": model_accuracy, "precision": model_precision, "recall": model_recall, "f1": model_f1 }

  return model_results

def compare_baseline_with_new_result(baseline_result, new_result):
  for key, value in baseline_result.items():
    print(f"Baseline {key}: {value:.2f}, New {key}: {new_result[key]:.2f}, Difference: {new_result[key] - value}")