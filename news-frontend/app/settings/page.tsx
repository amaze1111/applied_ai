"use client";

import { useState } from "react";
import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { Form, FormField, FormItem, FormLabel, FormControl, FormMessage } from "@/components/ui/form";

// Zod schema for validation
const settingsSchema = z.object({
  phone_number: z
    .string()
    .min(10, "Phone number must be 10 digits")
    .max(10, "Phone number must be 10 digits")
    .regex(/^\d{10}$/, "Phone number must be 10 digits"),
  keyword: z.string().min(1, "Please enter at least one topic"),
});

type SettingsFormValues = z.infer<typeof settingsSchema>;

export default function SettingsPage() {
  const [responseMsg, setResponseMsg] = useState("");
  const [error, setError] = useState("");

  const form = useForm<SettingsFormValues>({
    resolver: zodResolver(settingsSchema),
    defaultValues: {
      phone_number: "",
      keyword: "",
    },
  });

  async function onSubmit(values: SettingsFormValues) {
    setError("");
    setResponseMsg("");
    try {
      const res = await fetch("http://localhost:8000/summarize_and_send", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      });
      const data = await res.json();
      setResponseMsg(data.message || JSON.stringify(data));
    } catch (err) {
      setError("Error: " + err);
    }
  }

  return (
    <div className="max-w-md mx-auto mt-10">
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
          <FormField
            control={form.control}
            name="phone_number"
            render={({ field }) => (
              <FormItem>
                <FormLabel htmlFor="phone_number">Phone Number</FormLabel>
                <FormControl>
                  <Input
                    id="phone_number"
                    type="text"
                    placeholder="Enter your phone number"
                    maxLength={10}
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="keyword"
            render={({ field }) => (
              <FormItem>
                <FormLabel htmlFor="keyword">Topics</FormLabel>
                <FormControl>
                  <Textarea
                    id="keyword"
                    placeholder="Enter topic of interest"
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          {error && <div className="text-red-500">{error}</div>}
          {responseMsg && <div className="text-green-600">{responseMsg}</div>}
          <Button type="submit">Submit</Button>
        </form>
      </Form>
    </div>
  );
}