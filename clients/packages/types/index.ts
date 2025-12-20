import type { AxiosResponse } from 'axios'
import React from 'react'

declare const __brand: unique symbol

export type Branded<T, UniqueKey extends string> = T & { __brand: UniqueKey }

export type Nullable<T> = T | null

export type EnumType<T> = T[keyof T]

export type EmptyDictionary = Record<string, never>

export type Dictionary<T = unknown> = Record<string, T>

export type RequestResponse<T = unknown> = Promise<AxiosResponse<T>>

export type PartialBy<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>

export type Expand<T> = T extends infer O ? { [K in keyof O]: O[K] } : never

export type Timeout = ReturnType<typeof setTimeout>

export type OrderDirection = 'ASC' | 'DESC'

export type LogLevel = 'log' | 'warn' | 'error'

export type InjectProps<
	Key extends string,
	Value,
	Extras extends Record<string, any> = {},
> = {
	[K in Key]: Value
} & Extras

export type OnUploadProgress = (
	progress: number,
	uploaded: number,
	total: number,
) => void

export const ErrorType = {
	Validation: 'Validation',
	NotFound: 'NotFound',
	Null: 'Null',
	Forbidden: 'Forbidden',
	Internal: 'Internal',
	Unauthorized: 'Unauthorized',
	Failure: 'Failure',
	Conflict: 'Conflict',
	NotAllowed: 'NotAllowed',
} as const

export type ErrorType = EnumType<typeof ErrorType>

export interface ErrorObject {
	code: string
	message: string
	type: string
}

export type ErrorList = ErrorObject[]

export interface ResultResponse<T> {
	result: T
	errors: ErrorList
	isSuccess: boolean
	timestamp: string
}

export interface Paginated<T> {
	data: T[]
	meta: {
		itemsPerPage: number
		totalItems?: number
		currentPage?: number
		totalPages?: number
		sortBy: [string, OrderDirection][]
		searchBy: string[]
		search: string
		select: string[]
		filter?: {
			[column: string]: string | string[]
		}
		cursor?: string
	}
	links: {
		first?: string
		previous?: string
		current: string
		next?: string
		last?: string
	}
}

export interface PaginateQuery<
	F extends string = string,
	S extends string = string,
> {
	page?: number
	limit?: number
	sortBy?: [S, OrderDirection][]
	searchBy?: string[]
	search?: string
	filter?: {
		[column: F]: string | string[]
	}
	select?: string[]
	cursor?: string
	path?: string
}

export interface PagesListResponse<T> {
	pages: Paginated<T>[]
	pageParams: number[]
}

export type UnionToIntersection<U> = (
	U extends any ? (k: U) => void : never
) extends (k: infer I) => void
	? I
	: never

export type DetailedDivProps = React.DetailedHTMLProps<
	React.ButtonHTMLAttributes<HTMLDivElement>,
	HTMLDivElement
>

export type DetailedButtonProps = React.DetailedHTMLProps<
	React.ButtonHTMLAttributes<HTMLButtonElement>,
	HTMLButtonElement
>

export type DetailedInputProps = React.InputHTMLAttributes<HTMLInputElement>

export type DetailedSelectProps = React.DetailedHTMLProps<
	React.SelectHTMLAttributes<HTMLSelectElement>,
	HTMLSelectElement
>

export type DetailedLabelProps = React.DetailedHTMLProps<
	React.LabelHTMLAttributes<HTMLLabelElement>,
	HTMLLabelElement
>

export type DetailedTextareaProps = React.DetailedHTMLProps<
	React.TextareaHTMLAttributes<HTMLTextAreaElement>,
	HTMLTextAreaElement
>

export type ModelListField<T, U extends Dictionary<any>> = {
	count: number
	loading: boolean
	error: boolean
	fetching?: boolean
	list: T[]
	filter: U
	checked?: number[]
}

export type ModelListState<T, U extends Dictionary<any>> = {
	setCount: (count: number) => void
	setError: (error: boolean) => void
	setLoading: (loading: boolean) => void
	setFetching: (fetching: boolean) => void
	setChecked: (checked: number[]) => void
	setList: (list: T[]) => void
	setFilter: (filter: U) => void
	reset: () => void
} & ModelListField<T, U>