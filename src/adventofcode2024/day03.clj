(ns adventofcode2024.day03
  (:require
    [clojure.string :as str]))

(def sample1
  "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")

(def input (slurp "resources/input03"))

(def muls (map rest (re-seq #"mul\((\d{1,3}),(\d{1,3})\)" input)))

(defn parse-first [nums] (Integer/parseInt (first nums)))
(defn parse-last [nums] (Integer/parseInt (last nums)))

(def result
  (reduce + (map #(* (parse-first %) (parse-last %)) muls))
)


(println result)
