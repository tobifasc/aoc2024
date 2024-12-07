(ns adventofcode2024.day01
  (:require
    [clojure.string :as str]))

(def sample1
  "3   4
4   3
2   5
1   3
3   9
3   3")

(def input (slurp "resources/input01"))

(defn parse-row [rowstr]
  (map #(Integer/parseInt %) (str/split rowstr #"\s+"))
)

(def rows (map parse-row (str/split-lines input)))

(def left (map first rows))
(def right (map last rows))

(def freqs (frequencies right))

(def result (reduce + (map #(* % (get freqs % 0)) left)))

(println result)
